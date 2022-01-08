import { useRouter } from "next/router";

export default () => {
    const router = useRouter();

    const { patient_id } = router.query;
    return <div>Patient id: {patient_id}</div>
}