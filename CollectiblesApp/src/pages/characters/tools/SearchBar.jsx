import React from 'react';
import { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import styles from './SearchBar.module.scss';
import { searchForCharacters } from '../../../api/characters';

const SearchBar = () => {
    const [value, setValue] = useState('');
    const [suggestions, setSuggestions] = useState([]);
    const [hideSuggestions, setHideSuggestions] = useState(true);
    const [searchParams] = useSearchParams();
    const navigate = useNavigate();

    // Executed only once 
    // Checks is the url contains any search params
    useEffect(() => {
        if (searchParams.has('search')) {
            setValue(searchParams.get('search'));
        }
    }, []);

    // Executed when value changed and when search params changed
    // Get suggestions
    useEffect(() => {
        const fetchData = async () => {
            try {
                if (value != '') {
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

    // When confirm search
    // Changing url
    const onSearchButt = (e) => {
        e.preventDefault();
        navigate(`/characters/?search=${value}`);
    };

    // When user choose item from suggestion
    // set value as chosen
    // Calls confirm search
    const onSuggestionClick = (name) => (e) => {
        e.preventDefault();
        setValue(name);
        onSearchButt(e);
    };

    // To hide suggestion
    const handleFocus = () => {
        setHideSuggestions(false);
    };

    const handleBlur = () => {
        setTimeout(() => {
            setHideSuggestions(true);
        }, 200);
    };

    return (
        <>
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
                <div className={`${styles.suggestions} ${hideSuggestions && styles.hidden}`}>
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
        </>
    );
};

export default SearchBar;