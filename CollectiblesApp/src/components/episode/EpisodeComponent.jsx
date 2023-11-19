import React from 'react';

const EpisodeItem = (props) => {
    console.log(props);
  const episodeItemStyle = {
    display: 'flex',
    border: '1px solid #ccc',
    borderRadius: '8px',
    margin: '10px',
    padding: '10px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  };

  const episodeDetailsStyle = {
    marginLeft: '15px',
  };

  const characterImageStyle = {
    width: '50px',
    height: '50px',
    borderRadius: '50%',
    marginRight: '5px',
  };

  return (
    <div style={episodeItemStyle}>
      <img
        src="path/to/rick_and_morty_image.jpg"
        alt="Rick and Morty"
        style={{ width: '100px', height: '100px', borderRadius: '8px' }}
      />
      <div style={episodeDetailsStyle}>
        <h2>{props.message.name}</h2>
        <p>{`Episode: ${props.message.episode}`}</p>
        <p>{`Air Date: ${props.message.airDate}`}</p>
        <div>
            <img
              src={props.message.characters[0].image}
              alt={'none'}
              style={characterImageStyle}
            />
            <img
              src={props.message.characters[1].image}
              alt={'none'}
              style={characterImageStyle}
            />
        </div>
      </div>
    </div>
  );
};

export default EpisodeItem;