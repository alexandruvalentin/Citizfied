
const fetchApi = async (url, payload, success, fail) => {
    try {
        const response = await fetch(url, payload);
        if (response.ok) {
            response.json().then(success);
        }
    } catch (error) {
        fail(error);
    }
}
const countryElem = document.getElementById('country');
const cityElem = document.getElementById('city');

countryElem.addEventListener('change', () => {
    const countryCode = countryElem.value;
    if (countryCode) {
        const cityPayload = {
            "method": "GET"
        }

        fetchApi('/cities/' + countryCode, cityPayload, (response) => {
            cityElem.innerHTML = response.map(city => {
                return `<option value="${city}">${city}</option>`;
            }).join();
        }, (error) => {
            console.log(error)
        })
    }
});
