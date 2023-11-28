import React from "react";
import { Link } from "react-router-dom";
import styles from "./Pagination.module.scss";

const Pagination = ({ totalPages, currentPage }) => {
    const renderPageNumbers = () => {
        const pageNumbers = [];

        // Display up to 5 pages
        const startPage = Math.max(1, Math.min(currentPage - 2, totalPages - 4));
        const endPage = Math.min(totalPages, startPage + 4);

        // Display the first page
        if (startPage > 1) {
            pageNumbers.push(
                <Link key={1} to={`?page=${1}`} className={styles.square}>
                    {1}
                </Link>
            );
            if (startPage > 2) {
                // Display an ellipsis if there are more pages before the startPage
                pageNumbers.push(<span key="ellipsis-start">...</span>);
            }
        }

        // Display pages within the range
        for (let i = startPage; i <= endPage; i++) {
            pageNumbers.push(
                <Link
                    key={i}
                    to={`?page=${i}`}
                    className={i === currentPage ? styles.active : styles.square}
                >
                    {i}
                </Link>
            );
        }

        // Display the last page
        if (endPage < totalPages) {
            if (endPage < totalPages - 1) {
                // Display an ellipsis if there are more pages after the endPage
                pageNumbers.push(<span key="ellipsis-end">...</span>);
            }
            pageNumbers.push(
                <Link
                    key={totalPages}
                    to={`?page=${totalPages}`}
                    className={styles.square}
                >
                    {totalPages}
                </Link>
            );
        }

        return pageNumbers;
    };

    return (
        <div className={styles.pagination}>
            {totalPages > 1 && renderPageNumbers()}
        </div>
    );
};

export default Pagination;
