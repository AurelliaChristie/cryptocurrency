import React from 'react';

import { Navbar, Container, Nav, NavDropdown } from "react-bootstrap";

const NavBar = () => {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Container>
            <Navbar.Brand href="/">
                Crypto Wallets Dashboard
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="me-auto">
                <NavDropdown title="Rich List" id="collasible-nav-dropdown">
                    <NavDropdown.Item href="/richlist/btc">Bitcoin</NavDropdown.Item>
                    <NavDropdown.Item href="/richlist/eth">Ethereum</NavDropdown.Item>
                    <NavDropdown.Item href="/richlist/bsc">Binance Smart Chain</NavDropdown.Item>
                    <NavDropdown.Item href="/richlist/sol">Solana</NavDropdown.Item>
                    <NavDropdown.Item href="/richlist/avax">Avalanche</NavDropdown.Item>
                    <NavDropdown.Item href="/richlist/luna">Terra</NavDropdown.Item>
                </NavDropdown>
                </Nav>
                <Nav>
                <Nav.Link href="/signup">Sign Up</Nav.Link>
                <Nav.Link href="/login">
                    Log In
                </Nav.Link>
                </Nav>
            </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default NavBar;
