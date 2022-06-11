import axios from "axios";

const BASE_URL = "";
const REFRESH_TOKEN_URL = "";
const UNAUTHORIZED_STATUS = 401;

let accessToken = localStorage.getItem("hc-access-token") || "";
let refreshToken = localStorage.getItem("hc-refresh-token") || "";

const axiosInstance = axios.create({
  baseUrl: BASE_URL,
  timeout: 1000,
  headers: { Authorization: `Bearer ${accessToken}` },
});

let benignStatusesRange = {
  min: 200,
  max: 299,
};

benignStatusesRange = new Proxy(benignStatusesRange, {
  has(proxiedObj, prop) {
    return prop >= proxiedObj.min && prop <= proxiedObj.max;
  },
});

const mostRecentRequestInfo = [];
mostRecentRequestInfo.peek = function () {
  return this[this.length - 1];
};

// interceptor to add seamless acces-token renewal
axiosInstance.interceptors.response.use(
  // error-free responses are immediately frowarded to the axios caller.
  (resp) => resp,
  // authorization error responses are re-sent with a new acces-token,
  // or given up on if the refresh-token is dead too.
  async (error) => {
    // supposedly, this is what it's going to look like once the token has expired
    // in which case a new accessToken should be fetched.
    if (error.status === UNAUTHORIZED_STATUS) {
      let accessTokenUpdateResult = await fetch(BASE_URL + REFRESH_TOKEN_URL, {
        headers: {
          Authorization: `Bearer ${refreshToken}`,
        },
      }).then((resp) => {
        // if the refresh token is dead too,
        // get redirected to the login page
        if (resp.status === UNAUTHORIZED_STATUS) {
          return "Refresh token dead.";
        } else {
          return resp.json();
        }
      });

      if (accessTokenUpdateResult === "Refresh token dead.") {
        // this means that a new accessToken hasn't been issued
        // due to access token expiration, so, go to login page
        return Promise.reject("Refresh token dead.");
      } else {
        // update the access token and
        accessToken = accessTokenUpdateResult;
        localStorage.setItem("hc-access-token", accessToken);
        // resend the last request
        let refetchedResult = await fetch(
          // args[0] - is the url of the request
          BASE_URL + mostRecentRequestInfo.peek().args[0],
          {
            method: mostRecentRequestInfoInfo.peek().method,
          }
        );
        if (refetchedResult.status in benignStatusesRange) {
          const refetchedData = await refetchedResult.json();
          return Promise.resolve(refetchedData);
        } else {
          return Promise.reject(
            "Tried to refetch the data with a refreshed token: ",
            refetchedResult
          );
        }
      }
    } else {
      return Promise.reject(error);
    }
  }
);

// this is a dirty little trick to keep track of the
// axios requests to refetch them if one of them fails
// bc of access-token deading
axiosInstance = new Proxy(axiosInstance, {
  get(proxiedObj, prop) {
    if (typeof proxiedObj[prop] === "function") {
      return (...args) => {
        // intercepting the most resent axios method call
        // to resend the requset later
        mostRecentRequestInfo.push({ method: prop, args });
        return proxiedObj[prop](...args);
      };
    }
    return proxiedObj[prop];
  },
});

export default axiosInstance;
