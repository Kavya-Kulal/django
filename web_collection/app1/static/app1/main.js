
let aside = document.querySelector("aside");

function autoScroll() {
    aside.scrollLeft += 1;
    if (aside.scrollLeft >= aside.scrollWidth - aside.clientWidth) {
        aside.scrollLeft = 0; // Restart scrolling
    }
}

setInterval(autoScroll, 20);
        function toggleDropdown(event) 
        {
    event.stopPropagation();
    var menu = document.getElementById('dropdownMenu');
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
    console.log(menu.style.display); // Debugging
}


        document.addEventListener('click', function(event) {
            var dropdownMenu = document.getElementById('dropdownMenu');
            if (!event.target.closest('.user-section')) {
                dropdownMenu.style.display = 'none';
            }
        });

        const sidebar = document.getElementById("sidebar");
        const resizer = document.getElementById("resizer");
        const username = document.getElementById("username");

        let isResizing = false;

        resizer.addEventListener("mousedown", function (event) {
            isResizing = true;
            document.addEventListener("mousemove", resizeSidebar);
            document.addEventListener("mouseup", stopResizing);
        });

        function resizeSidebar(event) {
            if (isResizing) {
                let newWidth = event.clientX;
                if (newWidth >= 100 && newWidth <= 400) {
                    sidebar.style.width = newWidth + "px";
                    adjustUsername(newWidth);
                }
            }
        }

        function stopResizing() {
            isResizing = false;
            document.removeEventListener("mousemove", resizeSidebar);
            document.removeEventListener("mouseup", stopResizing);
        }

        function adjustUsername(width) {
            if (width < 180) {
                username.style.maxWidth = "40px";
            } else if (width < 250) {
                username.style.maxWidth = "80px";
            } else {
                username.style.maxWidth = "120px";
            }
        }
        function toggleMenu(event, menuId) {
            event.stopPropagation();
            let menu = document.getElementById(menuId);
            
            // Close all other dropdowns first
            document.querySelectorAll(".menu-dropdown").forEach(m => {
                if (m.id !== menuId) m.style.display = "none";
            });

            // Toggle the clicked menu
            menu.style.display = (menu.style.display === "block") ? "none" : "block";
        }

        // Close dropdown when clicking outside
        document.addEventListener("click", function () {
            document.querySelectorAll(".menu-dropdown").forEach(menu => {
                menu.style.display = "none";
            });
        });
        


        
        document.getElementById("showInputBtn").addEventListener("click", function() {
            var inputBox = document.getElementById("inputBox");
            if (inputBox.style.display === "none") {
                inputBox.style.display = "block";
            } else {
                inputBox.style.display = "none";
            }
            showInputBtn.addEventListener("click", function () {
                inputBox.style.display = "block";
                inputBox.focus();
             // Once shown, it will not hide again
             
            });
            
            inputBox.addEventListener("blur", function () {
                if (inputBox.value.trim() === "") { 
                    inputBox.style.display = "none";
                }
            });
        });
       
        document.addEventListener("DOMContentLoaded", function () {
            var menuButton = document.getElementById("menuButton");
            var dropdownMenu = document.getElementById("drop_down_for_collection");

            menuButton.addEventListener("click", function () {
                dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
            });

            // Close menu if clicking outside
            document.addEventListener("click", function (event) {
                if (!menuButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
                    dropdownMenu.style.display = "none";
                }
            });
        });
    

// Close menu when clicking outside
document.addEventListener("DOMContentLoaded", function () {
    fetchCollections(); // Fetch collections on page load
});

// Function to fetch collections from the server
function fetchCollections() {
    
    fetch("{% url 'get_collections' %}")  // Ensure this URL is correctly defined in Django's urls.py
        .then(response => response.json())
        .then(data => {
            // Sort collections by creation time (assuming the backend sends timestamps)
            data.collections.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));

            // Clear existing collections before adding (prevents duplicates)
            const container = document.getElementById("collectionsContainer");
            container.innerHTML = "";

            // Add each collection to UI
            data.collections.forEach(collection => {
                addCollectionToUI(collection.name);
            });
        })
        .catch(error => console.error("Error fetching collections:", error));
}

// Function to add a new collection to the UI
function addCollectionToUI(collectionName) {
    let newDiv = document.createElement("div");
    newDiv.classList.add("collection-item");

    newDiv.innerHTML = `
        <div class="collection-name">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-folder2" viewBox="0 0 16 16">
                <path d="M1 3.5A1.5 1.5 0 0 1 2.5 2h2.764c.958 0 1.76.56 2.311 1.184C7.985 3.648 8.48 4 9 4h4.5A1.5 1.5 0 0 1 15 5.5v7a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 1 12.5zM2.5 3a.5.5 0 0 0-.5.5V6h12v-.5a.5.5 0 0 0-.5-.5H9c-.964 0-1.71-.629-2.174-1.154C6.374 3.334 5.82 3 5.264 3zM14 7H2v5.5a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 .5-.5z"/>
            </svg>
            ${collectionName}
        </div>
        <button class="collection_menu" onClick="show_menu(event,this)">☰</button>
    
    <div class="collection_dropdown2" style="display: none;">
        <button class="rename">Rename</button>
        <button class="delete">Delete</button>
    </div>
        <button class="collection_menu" onClick="show_menu(event,this)">☰</button>
        
        
    `;

    document.getElementById("collectionsContainer").appendChild(newDiv);
    
    
}

// Handle Enter key to create a new collection
document.getElementById("inputBox").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        let collectionName = this.value.trim();

        if (collectionName) {
            fetch("{% url 'create_collection' %}", {
                method: "POST",
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    name: collectionName
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    fetchCollections(); // Refresh list to maintain order
                } else {
                    alert("Error creating collection.");
                }
            })
            .catch(error => console.error("Error creating collection:", error));

            this.value = ""; // Clear input field
        }
    }
});
document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("click", function () {
        closeAllMenus(); // Close menus when clicking outside
    });
});

function show_menu(event, button) {
    console.log("show_menu triggered");
    event.stopPropagation(); // Prevents closing when clicking inside

    // Find the existing menu inside the button's parent
    let menu = button.parentElement.querySelector(".collection_dropdown2");

    if (!menu) {
        console.log("Menu not found!");
        return;
    }

    // Toggle visibility
    if (menu.style.display === "none" || menu.style.display === "") {
        closeAllMenus(); // Close any other open menus first
        menu.style.display = "block"; // Show menu
    } else {
        menu.style.display = "none"; // Hide menu
    }
}

// Function to close all menus when clicking outside
function closeAllMenus() {
    document.querySelectorAll(".collection_dropdown").forEach(menu => {
        menu.style.display = "none"; // Hide all menus
    });
}

// Hide menu when clicking anywhere else
document.addEventListener("click", function () {
    closeAllMenus();
});











        

