import React from "react";
import styles from './ErrorComponent.module.scss'
import Header from "../header/Header";
import Footer from "../footer/Footer";
import Starfield from "../background/Starfield";

const ErrorComponent = ({ errorMessage }) => {
    if (errorMessage) {
        return <>
            <Header />
            <div className={styles.error}>
                <p>{errorMessage.status}</p>
                <div className={styles.body}>
                    <p>Error: {errorMessage.body.header}</p>
                    <p>Description: {errorMessage.body.body}</p>
                </div>
            </div>
            <Starfield />
        </>
    } else {
        return <>
            <Header />
            <div className={styles.error}>
                <p>404</p>
                <div className={styles.body}>
                    <p>Ops! We can't find it!</p>
                    <p>The page you are looking for might have been removed had it's name changed or is temporary unavailable</p>
                </div>
            </div>
            <Starfield />
        </>
    }
}

export default ErrorComponent;