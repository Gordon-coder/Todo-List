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

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
    children: [
      {index: true, Component: Home},
      {path: "about", Component: About},
    ]
  },
]);

const root = document.getElementById("root")!;

createRoot(root).render(
  <RouterProvider router={router} />,
);