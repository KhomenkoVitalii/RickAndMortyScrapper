import { useEffect, useState } from 'react';
import EpisodeItem from '../../components/episode/EpisodeItem';
import styles from './Episode.module.scss'
import { getSeasonsCountRequest } from '../../api/episode_requests'

const Episode = () => {
    const [episodesCount, setEpisodesCount] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await getSeasonsCountRequest()
                setEpisodesCount(response.json())
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        fetchData()
    }, [])


    return <>
        <div className={styles.body}>
            {episodesCount && console.log(episodesCount)}

        </div>
    </>
};

export default Episode;