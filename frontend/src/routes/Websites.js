//Lista de esportes presentes nas Olimpíadas
//Ao clicar em algum dos esportes aparece um menu apresentando todas as modalidades presentes
//O usuário deve escolher a modalidade que deseja e será redirecionado para a página da modalidade, onde existe uma lista de todos os atletas

import '../Styles/Websites.css';
import Box from '@material-ui/core/Box';
import Website from '../components/website';
import { useEffect, useState } from 'react';
import { api, apiMain } from '../services/api';
import Navbar from '../components/navbar';


function ListaWebsites() {
  const [
    websites,
    setWebsites
  ] = useState([]);

  const getWebsites = async () => {
    const res = await api.get("/website");
    setWebsites(res.data);
  };

  useEffect(() => {
    getWebsites();
  }, []);


  return (
    <div className="ListaWebsites">
      <Navbar />
      <Box display="flex" flexDirection="row">
        {
          websites.map(item => <Website>{item}</Website>)
        }
      </Box>

    </div>
  );
}

export default ListaWebsites;
