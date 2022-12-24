import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const moveTankForward = (): Promise<AxiosResponse<void>> => {
    return axios.post(API_ROOT + '/tank/forward');
}