// main.js

// Define variables for the input fields and preview div
const nameInput = document.querySelector('#id_name');
const jobInput = document.querySelector('#id_job');
const colorInput = document.querySelector('#id_color');
const imageInput = document.querySelector('#id_image');
const previewDiv = document.querySelector('#preview');

// Add event listeners to the input fields to update the preview div
nameInput.addEventListener('input', updatePreview);
jobInput.addEventListener('input', updatePreview);
colorInput.addEventListener('input', updatePreview);
imageInput.addEventListener('change', updatePreview);

// Define the updatePreview function that updates the preview div
function updatePreview() {
    const name = nameInput.value;
    const job = jobInput.value;
    const color = colorInput.value;
    const image = imageInput.files[0];
    
    // Clear the preview div
    previewDiv.innerHTML = '';
    
    // Create a new card element
    const card = document.createElement('div');
    card.classList.add('bg-white', 'rounded-lg', 'p-6', 'shadow', 'w-96');
    
    // Add the name and job elements to the card
    const nameEl = document.createElement('h2');
    nameEl.classList.add('text-2xl', 'font-bold', 'mb-4');
    nameEl.innerText = name;
    const jobEl = document.createElement('p');
    jobEl.classList.add('text-lg', 'text-gray-600', 'mb-4');
    jobEl.innerText = job;
    card.appendChild(nameEl);
    card.appendChild(jobEl);
    
    // Add the image to the card
    if (image) {
        const reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onloadend = () => {
            const imgEl = document.createElement('img');
            imgEl.classList.add('w-full', 'h-auto', 'mb-4');
            imgEl.src = reader.result;
            card.appendChild(imgEl);
        };
    }
    
    // Set the card background color
    card.style.backgroundColor = color;
    
    // Add the card to the preview div
    previewDiv.appendChild(card);
}
