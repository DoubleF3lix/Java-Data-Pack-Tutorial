// Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict
function toggleDropdown(button) {
    let dropdownContent = button.nextElementSibling;

    // Reset all carets
    let allDropdownButtons = document.getElementsByClassName("dropdownButton");
    for (const dropdownButton of allDropdownButtons) {
        dropdownButton.childNodes[1].outerHTML = "<i class=\"dropdownCaret fa fa-caret-right\"></i>";
    }

    // Close all open dropdowns
    let allDropdowns = document.getElementsByClassName("dropdownContainer");
    for (const dropdown of allDropdowns) {
        dropdown.style.maxHeight = null;
    }

    if (dropdownContent.style.maxHeight) {
        dropdownContent.style.maxHeight = null;
        button.childNodes[1].outerHTML = "<i class=\"dropdownCaret fa fa-caret-right\"></i>";
    } else {
        dropdownContent.style.maxHeight = dropdownContent.scrollHeight + "px";
        button.childNodes[1].outerHTML = "<i class=\"dropdownCaret fa fa-caret-down\"></i>";
    }
}

async function displaySidebar() {
    let sidebarLocation = "/Java-Data-Pack-Tutorial/pages/sidebar.html";
    const sidebarHTML = await fetch(sidebarLocation).then(r => r.text());
    let sidebar = document.getElementById("sidebar");
    sidebar.innerHTML = sidebarHTML;

    /*
    // Remove the active status on the old element(s) if it exists
    try {
        document.getElementsByClassName("active").classList.remove("active");
    } catch (TypeError) {
        console.log("No element with 'active' class exists. Ignoring.")
    }

    // If page is https://site.com/pages/test.html, this gets /pages/test.html
    let currentPage = window.location.href.replace(window.location.protocol + "//" + window.location.host, "");

    // Set the current sidebar element as active
    document.querySelector(`a[href="${currentPage}"]`).classList.add("active");
    */
}