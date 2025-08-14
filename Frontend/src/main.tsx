import { createRoot } from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router";
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';

const router = createBrowserRouter([
  {
    path: "/",
    Component: App,
  },
]);

const root = document.getElementById("root")!;

createRoot(root).render(
  <RouterProvider router={router} />,
);