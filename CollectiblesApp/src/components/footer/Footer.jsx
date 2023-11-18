import { Link } from 'react-router-dom'
import styles from './Footer.module.scss'

const Footer = () => {
    return <>
        <footer>
            <div className={styles.name}>
                <p>By Khomenko Vitalii</p>
            </div>
            <div className={styles.links}>
                <Link to="https://www.linkedin.com/in/vitalii-khomenko-860163255/"><img src='linkedin-icon.png' /></Link>
                <Link to="https://github.com/KhomenkoVitalii/"><img src='github-icon.svg' /></Link>
            </div>
        </footer>
    </>
}

export default Footer;