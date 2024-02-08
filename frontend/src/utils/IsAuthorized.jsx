import { useContext } from "react";
import { AppContext } from "../context/AppContext";

const IsAuthorized = () => {
    const [state] = useContext(AppContext);

    return state.is_authorized;
};

export default IsAuthorized;