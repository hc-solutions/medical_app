import * as React from "react"
import axios from "axios"
axios.defaults.baseURL = "http://auth.hc-solutions.local/";

type IPerson = {

  name: String,
  height: String,
  mass: String,
  hair_color: String,
  skin_color: String,
  eye_color: String,
  birth_year: String,
  gender: String,
  homeworld: String,
  films: Array<String>,
  species: Array<String>,
  vehicles: Array<String>,
  starships: Array<String>,
  created: String,
  edited: String,
  url: String,

}

export default function () {

  const [entities, setEntities] = React.useState([])

  React.useEffect(() => {
    // fetch("https://swapi.dev/api/people").then(res => {
    //   console.log("response: ", res)
    //   return res.json();
    // }).then(data => {
    //   console.log("got json response: ", data.results)
    //   setEntities(data.results.map((entry: IPerson, ind: Number) => (<div key={ind}> {entry.name}</div>)))
    // })

    axios({ method: "post", url: "auth/realms/backend-realm/protocol/openid-connect/auth" }).then(data => {
      console.log("AUTH ep response: ", data);
    })
      .catch(e => {
        console.error(e)
      })
    axios({ method: "post", url: "auth/realms/backend-realm/protocol/openid-connect/token" }).then(data => {
      console.log("TOKEN ep response", data);
    }).catch(e => {
      console.error(e)
    })
  }, [])

  return (
    <div>{entities}</div>
  )
}