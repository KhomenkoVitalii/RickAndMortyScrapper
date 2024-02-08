import React, { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

const Filtering = () => {
    const [selectedFilter, setSelectedFilter] = useState(null);
    const [searchParams, setSearchParams] = useSearchParams();

    const handleFilterChange = (fieldName) => {
        setSelectedFilter(fieldName);
    };

    useEffect(() => {
        // Update selectedFilter based on the URL parameters
        if (searchParams.has('ordering')) {
            setSelectedFilter(searchParams.get('ordering'));
            // TODO: set select option to the current
        }
    }, []);

    useEffect(() => {
        if (selectedFilter && selectedFilter != '') {
            // If 'ordering' parameter exists, update it
            searchParams.set('ordering', selectedFilter);
        } else {
            // If no filter selected, remove 'ordering' parameter
            searchParams.delete('ordering');
        }
        setSearchParams(searchParams);
    }, [selectedFilter, setSearchParams]);

    return (
        <>
            <select value={selectedFilter || undefined} onChange={(e) => handleFilterChange(e.target.value)}>
                <option value=''>Select Filter</option>
                <option value='name'>Name ascending</option>
                <option value='-name'>Name descending</option>
            </select>
        </>
    )
}


export default Filtering;