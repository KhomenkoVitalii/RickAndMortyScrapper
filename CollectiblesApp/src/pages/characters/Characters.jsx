import React, { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { getCharactersRequest } from "../../api/characters";
import styles from "./Characters.module.scss";
import Tools from "./tools/Tools";
import Card from "../../components/card/Card"

const Characters = () => {
    const [characters, setCharacters] = useState(null);
    const [searchParams] = useSearchParams();

    const getCharacters = useMemo(() => async () => {
        try {
            let request_params = '';
            if (searchParams.has('page')) {
                // If 'page' parameter was set up
                request_params += `&page=${searchParams.get('page')}`;
            }

            if (searchParams.has('search')) {
                // if 'search' parameter was set up
                request_params += `&search=${searchParams.get('search')}`;
            }

            if (searchParams.has('ordering')) {
                // if 'ordering' parameter was set up
                request_params += `&ordering=${searchParams.get('ordering')}`;
            }

            const response = await getCharactersRequest(request_params)
            const data = await response.json()
            console.log(data);
            setCharacters(data);
        } catch (error) {
            console.log("ERROR" + error);
        }
    });

    useEffect(() => {
        const fetchData = async () => {
            getCharacters()
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