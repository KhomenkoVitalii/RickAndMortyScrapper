const homeRequest = async () => {
    const url = "http://127.0.0.1:8000/home/";
    const response = await fetch(url);
    return response;
}

export default homeRequest;