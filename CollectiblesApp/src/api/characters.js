import BackendPath from "./backend_path"

const getCharacters = (page) => {
    const URL = BackendPath.CHARACTERS + `?page=${page}`;
    return fetch(URL);
}

const searchForCharacters = (keyword) => {
    const URL = BackendPath.CHARACTERS + `?search=${keyword}`;
    return fetch(URL);
}

export { getCharacters, searchForCharacters };