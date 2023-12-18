async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(error);
    }
}

// Call the function and store the result in a variable
fetchData().then(data => {
    // You can use the data here
    console.log(data);
});