import { createRoot } from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router";
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import Home from './Home';
import About from './About';
import {Register, Login} from './Auth';

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      {index: true, Component: Home},
      {path: "about", Component: About},
      {path: "register", Component: Register},
      {path: "login", Component: Login},
    ]
  },
]);

const root = document.getElementById("root")!;

createRoot(root).render(
  <RouterProvider router={router} />,
);
