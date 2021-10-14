import Box from '@material-ui/core/Box';
import { useEffect, useState } from 'react';
import { api, apiMain } from '../services/api';
import Navbar from '../components/navbar';

function ListaSetores(props) {

    console.log(props);

  const [
    setores,
    setSetores
  ] = useState([]);

  const getSetores = async () => {
    const res = await apiMain.get(`/listar/setores/${props.match.params.idwebsite}`);
    setSetores(res.data);
    console.log('--------------setores-------------')
    console.log(res.data)
  }

  useEffect(() => {
    getSetores();
  }, []);

  return (
    <div className="ListaSetores">
      <div>
        <Navbar />
        <Box display="flex" flexDirection="row">
            <div id="ItemLista_Setor">
                <ul>

                    {
                    setores.map(item => <li>{item}</li>)
                    }

                </ul>
            </div>
        </Box>
      </div>
    </div>
  );
}

export default ListaSetores;