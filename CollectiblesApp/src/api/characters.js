import BackendPath from "./backend_path"

const getCharacters = (request_params) => {
    const URL = BackendPath.CHARACTERS + request_params;
    return fetch(URL);
}

const searchForCharacters = (keyword) => {
    const URL = BackendPath.CHARACTERS + `search=${keyword}`;
    return fetch(URL);
}

export { getCharacters, searchForCharacters };