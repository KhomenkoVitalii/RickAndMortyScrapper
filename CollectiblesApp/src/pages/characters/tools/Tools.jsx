import React from "react";
import styles from './Tools.module.scss';
import SearchBar from './SearchBar';
import Filtering from './Filtering'

const Tools = () => {


    return (
        <>
            <Filtering />
            <SearchBar />

            <div className={styles.pages}>
                {/* TODO: Implement pages */}
            </div>
        </>
    );
};

export default Tools;
