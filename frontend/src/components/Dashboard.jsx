import React, { useEffect, useState } from 'react';

function Dashboard() {
  const [shows, setShows] = useState([]);

  useEffect(() => {
    fetch('/api/shows')
      .then(res => res.json())
      .then(data => setShows(data));
  }, []);

  return (
    <ul>
      {shows.map(show => (
        <li key={show.id}>{show.title} - {show.host}</li>
      ))}
    </ul>
  );
}

export default Dashboard;
