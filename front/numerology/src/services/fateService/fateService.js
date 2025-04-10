import api from "../axiosInstance"; 

// Базовый URL для всех запросов
const BASE_URL = "https://matrixaaa.duckdns.org";

// Функция для обработки ошибок
const handleError = (error) => {
    console.error("Ошибка при получении данных:", error.message);
    throw error;
};

// 📌 Функция для расчёта матрицы судьбы
export const calculateNumerology = async ({ day, month, year }) => {
    try {
        const response = await api.post(`${BASE_URL}/matrix_fate/calculate-matrix/`, {
            day,
            month,
            year,
            category:'matrix_fate'
        });
        return response.data.matrix;
    } catch (error) {
        handleError(error);
    }
};

// 📌 Функция для получения данных качеств
export const getQualitiesData = async ({ a, b, c }) => {

    
    try {
        const params = {
            birth_a: a,
            mature_c: c,
            youth_b: b,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/personal_qualities/1/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getSoulWorkData = async ({ a, b, c }) => {
    try {
        const params = {
            developed : a ,
            innate: c,
            revealed: b,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/soul_work/5/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getKarmaData = async ({ d2, d1, d }) => {
    try {
        const params = {
            after: d2 ,
            before: d1,
            main: d,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/main_task_40/6/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
};

export const getPastLife=async({d1,d2,d})=>{
    try{
        const params={
            lesson:d1,
            experience:d2,
            main:d
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/past_life_task/9/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}
// 
export const getComfortPoint=async({e})=>{
    try{
        const params={
            comfort:e,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/soul_comfort_point/7/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}


export const getSelfRealization=async({a2})=>{
    try{
        const params={
            realization :a2,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/self_realization/8/talents/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
    
}

export const getPointPersonalPower=async({e})=>{
    try{
        const params={
            order :e,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/personal_power_point/10/personal_power_point/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }


    
}
export const getGenericPower=async({e1})=>{
    try{
        const params={
            order:e1,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/ancestral_power/11/ancestral_power/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getParentChildKarma=async({a2,a,a1})=>{
    try{
        const params={
            mistakes:a2,
            teach:a,
            growth:a1,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/parent_child_karma/12/parent_child_karma/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getSpiritualKarma=async({b,b1,b2})=>{
    try{
        const params={
            task1:b,
            task2:b1,
            task3:b2,
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/spiritual_karma/13/spiritual_karma/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getMatrixRelationship=async({k,d2,j})=>{
    try{
        const params={
            meeting:k,
            tasks:d2,
            partner:k,
            problems:j
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/matrix_relationships/14/matrix_relationships/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getMatrixMoney=async({l,j,c2})=>{
    try{
        const params={
            blocks:j,
            money:l,
            unblock:j,
            tasks2:c2,
            professions:c2,
            tasks1:l
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/matrix_money/15/matrix_money/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getSoulMission=async({r,s,y,t,u,v,w})=>{
    try{
        const params={
            p1:r,
            p2:s,
            p3:y,
            s1:t,
            s2:u,
            s3:v,
            spiritual:w
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/soul_mission/16/soul_mission/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getDiseasePredisposition=async({h,i,a,b,c})=>{
    try{
        const params={
            a1:a,
            a2:b,
            a3:c,
            paternal:h,
            maternal:i, 
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/disease_predisposition/17/disease_predisposition/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}

export const getHealthMap=async({o6,p6,q6,o4,p4,q4,o3,p3,q3,o1,p1,q1,o7,p7,q7,o2,p2,q2,o,p,q,o5,p5,q5})=>{
    try{
        const params={
            o6:o6,
            p6:p6,
            q6:q6,
            o4:o4,
            p4:p4,
            q4:q4,
            o3:o3,
            p3:p3,
            q3:q3,
            o1:o1,
            p1:p1,
            q1:q1,
            o7:o7,
            p7:p7,
            q7:q7,
            o2:o2,
            p2:p2,
            q2:q2,
            o:o,
            p:p,
            q:q,
            o5:o5,
            p5:p5,
            q5:q5  
        };
        const response = await api.get(`${BASE_URL}/matrix_fate/health_map/2/health_map/`, { params });
        return response.data;
    } catch (error) {
        handleError(error);
    }
}






