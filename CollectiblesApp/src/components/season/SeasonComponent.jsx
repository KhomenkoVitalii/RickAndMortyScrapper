import styles from './SeasonComponent.module.scss'
import React from 'react';
import { Link } from 'react-router-dom'

const SeasonComponent = ({ number }) => {
    const link = `?season=${number}`
    return <>
        <div className={styles.body}>
            <Link to={link}>
                <p>Season: {number}</p>
            </Link>
        </div>
    </>
}

export default SeasonComponent;