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

    return (
        <>
            <div className={styles.offer}>
                <p>COLLECT THEM ALL</p>
            </div>
            <div className={styles.body}>
                {data && <Card message={data.characters[0]} />}
                {data && <Card message={data.characters[1]} />}
                {data && <Card message={data.characters[2]} />}
                {data && <Card message={data.characters[3]} />}
            </div>
        </>
    );
}

export default Home;
