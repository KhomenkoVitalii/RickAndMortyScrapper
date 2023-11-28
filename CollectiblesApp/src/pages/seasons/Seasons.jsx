import { useEffect, useState, useMemo } from 'react';
import styles from './Seasons.module.scss';
import { getSeasonsCountRequest, getSeasonEpisodesRequest } from '../../api/episode_requests';
import SeasonComponent from '../../components/season/SeasonComponent';
import { useSearchParams } from 'react-router-dom';
import EpisodeItem from '../../components/episode/EpisodeItem';

const Seasons = () => {
    const [seasonsCount, setSeasonsCount] = useState(null);
    const [seasonEpisodes, setSeasonEpisodes] = useState(null);
    const [searchParams] = useSearchParams();

    const getEpisodes = useMemo(() => async () => {
        try {
            const response = await getSeasonEpisodesRequest(searchParams.get('season'));
            const data = await response.json();
            setSeasonEpisodes(data);
            console.log(data);
        } catch (error) {
            console.error('Error fetching episodes:', error);
        }
    }, [searchParams]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                if (searchParams.has('season')) {
                    await getEpisodes();
                } else {
                    const response = await getSeasonsCountRequest();
                    const data = await response.json();
                    const num = Number(data.season_number);
                    setSeasonsCount(num);
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, [searchParams, getEpisodes]);


    // get the 'season' parameter from the URL
    const seasonParam = searchParams.get('season');

    // If not exists, display seasons
    if (!seasonParam) {
        // If data loaded
        if (seasonsCount) {
            return (
                <div className={styles.body}>
                    {Array.from({ length: seasonsCount }, (_, index) => (
                        <SeasonComponent key={index} number={index + 1} />
                    ))}
                </div>
            );
        }
        // if not
        return (
            // TODO: Add loader or your existing content
            <p>Loading...</p>
        );
    }

    // If episodes exist, display episodes of the season
    if (seasonEpisodes) {
        return (
            <>
                <div className={styles.episodes}>
                    {Array.from(seasonEpisodes, (episode, index) => (
                        <EpisodeItem key={index} props={episode} />
                    ))}
                </div>
            </>
        );
    } else {
        // If episodes don't exist, display a loading message
        return <p>Loading...</p>;
    }
};

export default Seasons;
