import * as React from "react";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import ShareIcon from "@mui/icons-material/Share";
import FavoriteIcon from "@mui/icons-material/Favorite";
import { useGlobalContext } from "./StateContext";
import MoreVertIcon from '@mui/icons-material/MoreVert';
import { useNavigate } from 'react-router-dom';

const MoviesList = () => {
  const {
    state: { currYear },
  } = useGlobalContext();

  const navigate = useNavigate();

  const [movies, setMovies] = React.useState([]);
  React.useEffect(() => {
    // Define the fetch function
    if (!!currYear) {
      (async () => {
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/movies/year/${currYear}`
          ); // Replace with your API endpoint
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          const data = await response.json();
          setMovies(data);
        } catch (error) {
          console.log(error);
        }
      })();
    }
  }, [currYear]);
  const handleButtonClick = (_id) => {
    navigate(`/detail/${_id}`);
  };


  return (
    <div
      style={{
        textAlign: "start",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      {movies.map((movie, index) => (
        <Card key={index} style={{ marginBottom: 10, width: "50%" }}>
          <CardContent style={{ paddingBottom: 10 }}>
            <CardHeader
              avatar={<Avatar sx={{ bgcolor: [500] }}>{movie.title[0]}</Avatar>}
              title={
                <Typography variant="h5" component="h2">
                  {movie.title}
                </Typography>
              }
              subheader={`Year: ${movie.year}`}
            />
            <CardMedia
              component="img"
              height={300}
              image={movie.poster}
              alt="Not Avaliable"
            />
            <Typography variant="body2" component="p">
              {movie.description}
            </Typography>
            <CardActions disableSpacing>
              <IconButton aria-label="add to favorites">
                <FavoriteIcon />
              </IconButton>
              <IconButton aria-label="share">
                <ShareIcon />
              </IconButton>
              <IconButton onClick={() => handleButtonClick(movie._id)} style={{ marginLeft: 'auto' }}>
                <MoreVertIcon />
              </IconButton>
            </CardActions>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default MoviesList;
