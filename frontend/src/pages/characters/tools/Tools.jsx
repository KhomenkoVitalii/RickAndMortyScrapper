import React from "react";
import styles from './Tools.module.scss';
import SearchBar from './SearchBar';
import Filtering from './Filtering'
import Pagination from "./Pagination";

const Tools = ({ totalPages, currentPage }) => {


    return (
        <>
            <Filtering />
            <SearchBar />
            <Pagination totalPages={totalPages} currentPage={currentPage} />
        </>
    );
};

export default Tools;
