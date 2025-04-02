// index.js

// Function to create and display navigation links
function createNavigation() {

    const navContainer = document.getElementById('nav-container'); // Container for the nav links
    //const welcomeMessage = document.createElement('h1');

    const pages = [
        { name: "Income", url: " " },
        { name: "Blog", url: " " }, 
        { name: "Logout", url: " " },
        // Add more pages as needed
    ];

    // Create a list of navigation links
    pages.forEach(page => {
        const link = document.createElement('a');
        link.textContent = page.name;
        link.href = page.url;  // Set the URL for navigation
        link.classList.add('nav-links');  // Optional: add CSS class for styling
        navContainer.appendChild(link);  // Append the link to the container
    });
}

// Run the function to create navigation links when the page loads
document.addEventListener('DOMContentLoaded', createNavigation);
