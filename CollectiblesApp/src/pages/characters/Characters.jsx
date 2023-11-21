import React, { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { getCharacters } from "../../api/characters";
import styles from "./Characters.module.scss";

const Characters = () => {
    const [characters, setCharacters] = useState(null);
    const [searchParams] = useSearchParams();

    const getEpisodes = useMemo(() => async () => {
        try {
            const response = await getCharacters(1)
            const data = await response.json()
            console.log(data);
            setCharacters(data);
        } catch (error) {
            console.log("ERROR" + error);
        }
    });

    useEffect(() => {
        const fetchData = async () => {
            getEpisodes()
        };
        fetchData();
    }, [searchParams]);

    return <>
        <div className={styles.body}>
            <div className={styles.header}>

            </div>
            <div className={styles.items}>

            </div>
        </div>
    </>
}

export default Characters;