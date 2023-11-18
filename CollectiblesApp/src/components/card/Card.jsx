import { Link } from 'react-router-dom';
import styles from './Card.module.scss';
import { useState } from 'react';

const Card = (props) => {
    const [isHovered, setHover] = useState(false);
    const [rotateX, setRotateX] = useState(0);
    const [rotateY, setRotateY] = useState(0);

    const handleHoverToggle = () => {
        setHover(!isHovered);
    };

    const handleMouseMove = (e) => {
        const { clientX, clientY, target } = e;
        const { left, top, width, height } = target.getBoundingClientRect();

        const percentX = (clientX - left) / width - 0.5;
        const percentY = (clientY - top) / height - 0.5;

        setRotateX(percentY * 35);
        setRotateY(percentX * 35);
    };

    const item = props.message;
    const item_image_path = "http://127.0.0.1:8000" + item.image;

    return (
        <div
            className={`${styles.card} ${isHovered ? styles.hovered : ''}`}
            onMouseEnter={handleHoverToggle}
            onMouseLeave={handleHoverToggle}
            onMouseMove={handleMouseMove}
            style={{
                transform: `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(${isHovered ? 1.3 : 1})`,
            }}
        >
            <img src={item_image_path} alt={item.name} />
            <Link to={item.url}>
                <p>Name: {item.name}</p>
            </Link>
        </div>
    );
};

export default Card;
