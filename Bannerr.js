import React from 'react'
import banner from "../assets/images/banimg.png";
import "../style/Banner.css"

const Banner = () => {
    return (
        <div className="banner">
            <img src={banner} alt="Banner-img" />
        </div>
    )
}

export default Banner
