import { Link } from 'react-router-dom'
import styles from './Header.module.scss'

const Header = () => {
    return <>
        <header>
            <div className={styles.logo}>
                <Link to='/'>
                    <img src="/Logo.svg" />
                    <div className={styles.logoText}>
                        <p>Rich and Morty</p>
                        <p>collectibles</p>
                    </div>
                </Link>
            </div>
            <div className={styles.links}>
                <Link to='/'>Home</Link>
                <Link to='/seasons/'>Seasons</Link>
                <Link to='/characters/'>Characters</Link>
                <Link to='/my-collection/'>My collections</Link>
            </div>
        </header>
    </>
}

export default Header;