import React from 'react';
import styles from './EpisodeItem.module.scss'

const EpisodeItem = ({ props }) => {
  return (
    <>
      <div className={styles.item}>
        <h2>{props.name}</h2>
        <p>{`${props.episode}`}</p>
        <p>{`${props.air_date}`}</p>
        <div className={styles.images}>
          {props.characters.map((character, index) => (
            <img key={index} src={character.image} alt={character.name} />
          ))}
        </div>
      </div>
    </>
  );
}

export default EpisodeItem;