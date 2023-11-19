import EpisodeItem from '../../components/episode/EpisodeComponent';
import styles from './Episode.module.scss'

const Episode = () => {
    return <>
        <div className={styles.body}>
            <EpisodeItem message={{
                name: 'Pilot',
                episode: 'S01E01',
                airDate: 'wed 01',
                characters: [
                    {
                        image: 'https://rickandmortyapi.com/api/character/avatar/1.jpeg',
                    },
                    {
                        image: 'https://rickandmortyapi.com/api/character/avatar/2.jpeg'
                    }
                ]
            }}/>
        </div>
    </>
};

export default Episode;