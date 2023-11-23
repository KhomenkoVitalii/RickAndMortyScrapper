import React, { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { getCharacters } from "../../api/characters";
import styles from "./Characters.module.scss";
import Tools from "./tools/Tools";
import Card from "../../components/card/Card"

const Characters = () => {
    const [characters, setCharacters] = useState(null);
    const [searchParams] = useSearchParams();

    const getEpisodes = useMemo(() => async () => {
        try {
            // if (searchParams.has('page'))
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
                <Tools />
            </div>
            <div className={styles.items}>
                {characters && characters.results.map((character, key) => (
                    <Card key={key} message={character} />
                ))}
            </div>
        </div>
    </>
};

export default Characters;