import React from 'react';
import { useState } from 'react';

import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

import { api, apiMain } from '../services/api';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        ProblemFinder
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  title: {
    marginBottom: theme.spacing(2),
  },
}));


export default function Cadastro() {
  const classes = useStyles();

  const [UsuarioEmail, setEmail] = useState('');
  const [UsuarioSenha, setSenha] = useState('');
  const [UsuarioNome, setNome] = useState('');
  const [UsuarioSobrenome, setSobrenome] = useState('');
  const [UsuarioAlertas, setAlertas] = useState(false);
  const [isPending, setIsPending] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault();
    const usuario = { UsuarioNome, UsuarioSobrenome, UsuarioEmail, UsuarioSenha, UsuarioAlertas };

    setIsPending(true);

    fetch(api + '/usuario', {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(usuario)
    }).then(() => {
      console.log("Novo usuário cadastrado.");
      setIsPending(false);
    })
  }

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Typography component="h1" variant="h5" className={classes.title}>
          Participe da nossa comunidade e comece a fazer a diferença!
        </Typography>
        <form className={classes.form} noValidate onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                required
                fullWidth
                id="firstName"
                label="Nome"
                autoFocus
                value={UsuarioNome}
                onChange={(e) => setNome(e.target.value)}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="lastName"
                label="Sobrenome"
                name="lastName"
                autoComplete="lname"
                value={UsuarioSobrenome}
                onChange={(e) => setSobrenome(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="Endereço de Email"
                name="email"
                autoComplete="email"
                value={UsuarioEmail}
                onChange={(e) => setEmail(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Senha"
                type="password"
                id="password"
                autoComplete="current-password"
                value={UsuarioSenha}
                onChange={(e) => setSenha(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox value={!UsuarioAlertas} color="primary" />}
                label="Eu desejo receber notificações, alertas e anúncios sobre novas oportunidades."
                onChange={e => setAlertas(e.target.value)}
              />
            </Grid>
          </Grid>
          { !isPending &&
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Participar
            </Button>
           }
           { isPending &&
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              disabled
              href="/"
            >
              Você está sendo cadastrado...
            </Button>
           }
          <Grid container justifyContent="flex-end">
            <Grid item>
              <Link href="/" variant="body2">
                Já possui uma conta? Entre no site
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyright />
      </Box>
    </Container>
  );
}