// Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict
function toggleDropdown(button) {
    button.classList.toggle("active");
    let dropdownContent = button.nextElementSibling;
    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
        // Modify the caret
        button.childNodes[1].outerHTML = "<i class=\"dropdownCaret fa fa-caret-right\"></i>";
    } else {
        dropdownContent.style.display = "block";
        // Modify the caret
        button.childNodes[1].outerHTML = "<i class=\"dropdownCaret fa fa-caret-down\"></i>";
    }
}

async function displaySidebar() {
    let sidebarLocation = "/java_data_pack_tutorial/pages/sidebar.html";
    const sidebarHTML = await fetch(sidebarLocation).then(r => r.text());
    let sidebar = document.getElementById("sidebar");
    sidebar.innerHTML = sidebarHTML;

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
}