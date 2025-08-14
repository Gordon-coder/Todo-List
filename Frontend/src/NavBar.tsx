import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

type NavBarProps = {
  loggedIn: boolean;
};

function NavBar({loggedIn}: NavBarProps) {
  return (
    <Navbar bg="light" expand="lg" className="p-2">
      <Navbar.Brand href="#home">Todo List</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/about">About</Nav.Link>
          {
            loggedIn ? (
              <Nav.Link href="/logout">Logout</Nav.Link>
            ) : (
              <>
                <Nav.Link href="/login">Login</Nav.Link>
                <Nav.Link href="/register">Register</Nav.Link>
              </>
            )
          }
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavBar;