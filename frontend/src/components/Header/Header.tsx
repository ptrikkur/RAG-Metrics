import { Header as CarbonHeader, HeaderName, HeaderNavigation, HeaderMenuItem } from '@carbon/react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <CarbonHeader aria-label="RAG Metrics Calculator">
      <HeaderName as={Link} to="/" prefix="">
        <img 
          src="/assets/ibm-bob-logo.svg" 
          alt="IBM Bob" 
          className="header-logo"
        />
        <span className="header-title">RAG Metrics Calculator</span>
      </HeaderName>
      <HeaderNavigation aria-label="Main Navigation">
        <HeaderMenuItem as={Link} to="/">
          Home
        </HeaderMenuItem>
        <HeaderMenuItem as={Link} to="/saved">
          Saved Analyses
        </HeaderMenuItem>
      </HeaderNavigation>
    </CarbonHeader>
  );
};

export default Header;

// Made with Bob
