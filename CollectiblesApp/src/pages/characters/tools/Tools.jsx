import React, { useEffect, useState } from "react";
import styles from './Tools.module.scss'
import SearchBar from './SearchBar'

const Tools = () => {
    return (
        <>
            <button
                className={styles.filter}
                onClick={() => { console.log("Hihi-Haha"); }}>
                Order by "Name"
                <img src="/arrow_up.svg" alt="filter" />
            </button>

            <SearchBar />

            <div className={styles.pages}>

            </div>
        </>
    )
};

export default Tools;