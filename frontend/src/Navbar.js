import React from 'react';
import { Outlet, NavLink } from "react-router-dom";
import { SiYourtraveldottv } from 'react-icons/si'
function Navbar(props) {
    return (
        <nav className='h-auto'>
        <div className=' fixed container bg-gradient-to-r from-navcolor1 to-navcolor2 font-bold text-neutral-100 z-50'>
           
            <div className="flex gap-40 h-15 text-lg py-6">
             <div className="basis-1/3 px-8 font-Raleway flex inline-flex gap-4 text-2xl font-normal tracking-wider">
                  
             <NavLink className="flex" to="/home"><span >
                 < SiYourtraveldottv className='h-8 w-8 mx-4'/>
                      {/* <svg xmlns="http://www.w3.org/2000/svg" className="h-9 w-9" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
  <path strokeLinecap="round" strokeLinejoin="round" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
</svg> */}
</span>Swing</NavLink></div>
             <div className="basis-2/3 items-center font-Poppins font-normal"><ul className='inline-flex gap-12 float-right pr-8'>
               <li> <NavLink to="/home">Home</NavLink></li>
               <li> <NavLink to="/travel">Travel</NavLink></li>
               <li> <NavLink to="/offers">Offers</NavLink></li>
               <li> <NavLink to="/contact">Contact</NavLink></li>
           </ul></div>
</div>

        </div>
        </nav>
    );
}

export default Navbar;