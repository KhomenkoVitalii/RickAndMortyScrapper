import React, { useEffect, useState } from 'react';
import Card from '../../components/card/Card'
import homeRequest from '../../api/home_request';
import styles from './Home.module.scss'

const Home = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await homeRequest();
                const jsonData = await response.json();
                setData(jsonData);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    if (!data) {
        // TODO: Place there <Loading/> component
        return <p>Loading...</p>;
    }

    return (
        <>
            <div className={styles.offer}>
                <h1>COLLECT THEM ALL</h1>
            </div>
            <div className={styles.body}>
                <Card message={data.characters[0]} />
                <Card message={data.characters[1]} />
                <Card message={data.characters[2]} />
                <Card message={data.characters[3]} />
            </div>
        </>
    );
}

export default Home;
