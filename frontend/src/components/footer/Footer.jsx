import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Footer.module.scss';

const Footer = () => {
    return (
        <footer className={styles.footer}>
            <div className={styles.name}>
                <p>By Khomenko Vitalii</p>
            </div>
            <div className={styles.links}>
                <Link to="https://www.linkedin.com/in/vitalii-khomenko-860163255/" target="_blank" rel="noopener noreferrer">
                    <img src='linkedin-icon.png' alt="LinkedIn Icon" />
                </Link>
                <Link to="https://github.com/KhomenkoVitalii/" target="_blank" rel="noopener noreferrer">
                    <img src='github-icon.svg' alt="GitHub Icon" />
                </Link>
            </div>
        </footer>
    );
}

export default Footer;
