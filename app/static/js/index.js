const baseUrl = 'http://127.0.0.1:8000/api/v1/catalog'

const modal = document.getElementById('productModal');
const addProductBtn = document.getElementById('addProductBtn');
const closeModal = document.getElementById('closeModal');
const productForm = document.getElementById('productForm');
const productsTable = document.querySelector('.products-table');
const headerTableResults = document.querySelector('.products-table__header');

modal.style.display = 'none';


document.addEventListener('DOMContentLoaded', async () => {
    
    addProductBtn.onclick = function () {
        modal.style.display = 'flex';
    };

    closeModal.onclick = function () {
        modal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    let products = await getProducts();
    let data = await products.json();
    
    data.forEach(product => {
        let title = product.title;
        let description = product.description;
        let price = product.price;
        addProductInTable(title, description, price);
    })
    
});

productForm.onsubmit = async function (e) {
    e.preventDefault();

    const title = document.getElementById('productName').value;
    const description = document.getElementById('productDescription').value;
    const price = document.getElementById('productPrice').value;

    addProductInTable(title, description, price);
    await createProduct(title, description, price);

    modal.style.display = 'none';
    productForm.reset();
};

async function getProducts() {
    return await fetch(`${baseUrl}/products/`);
    }

function addProductInTable(title, description, price) {
    if (!title.trim()) {
        alert('Название не может быть пустым.');
        return;
    }

    if (price < 0) {
        alert('Цена не может быть меньше 0.');
        return;
    }

    let codeTableRow = `
        <tr>
            <td>${title}</td>
            <td>${description}</td>
            <td>${price}</td>
        </tr>
    `

    headerTableResults.insertAdjacentHTML("afterend", codeTableRow);
}

async function createProduct(title, description, price) {
    
    try {
        
        const response = await fetch(`${baseUrl}/products/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                description: description,
                price: price
            })
        });

        const data = await response.json();

        console.log(data);
    } catch(error) {   
        console.log(error)
    } 
}