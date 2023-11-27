import React from 'react';
import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import styles from './SearchBar.module.scss';
import { searchForCharacters } from '../../../api/characters';

const SearchBar = () => {
    const [value, setValue] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const [hideSuggestions, setHideSuggestions] = useState(true);
    const [searchParams, setSearchParams] = useSearchParams();

    useEffect(() => {
        if (searchParams.has('search')) {
            setValue(searchParams.get('search'));
        }
    }, [searchParams]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                if (value !== '') {
                    const response = await searchForCharacters(value);
                    const data = await response.json();
                    setSuggestions(data.results);
                }
            } catch (error) {
                console.log(error);
            }
        };

        fetchData();
    }, [value, searchParams]);

    const changeUrl = (url) => {
        if (url && url !== '') {
            searchParams.set('search', url);
        } else if (value !== '') {
            searchParams.set('search', value);
        } else {
            searchParams.delete('search');
        }
        setSearchParams(searchParams);
    };

    const onSearchButt = (e) => {
        e.preventDefault();
        changeUrl();
    };

    const onSuggestionClick = (name) => (e) => {
        e.preventDefault();
        setValue(name);
        changeUrl(name);
    };

    const handleBlur = () => {
        setHideSuggestions(true);
    };

    const handleFocus = () => {
        // Set hideSuggestions to false when focused
        setHideSuggestions(false);
    };

    // Define a separate style object for visible suggestions
    const visibleSuggestionsStyle = hideSuggestions ? { visibility: 'hidden' } : {};

    return (
        <div className={styles.container}>
            <form>
                <input
                    onFocus={handleFocus}
                    onBlur={handleBlur}
                    type="text"
                    className={styles.textbox}
                    placeholder="Search data..."
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                />
                <button onClick={onSearchButt}><img src='/search-icon.svg' alt="search icon" /></button>
            </form>
            <div className={styles.suggestions} style={visibleSuggestionsStyle}>
                {suggestions.map((suggestion) => (
                    <div
                        key={suggestion.id}
                        className={styles.suggestion}
                        onClick={onSuggestionClick(suggestion.name)}
                    >
                        <p>{suggestion.name}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SearchBar;
